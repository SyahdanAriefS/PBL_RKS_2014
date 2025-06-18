$(document).ready(function() {
    if ( $.fn.DataTable.isDataTable('#victimTable') ) {
        $('#victimTable').DataTable().clear().destroy();
    }
    $('#victimTable').DataTable({
        pageLength: 10,
        searching: true
    });
});
