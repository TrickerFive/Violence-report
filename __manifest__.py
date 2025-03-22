{
    'name' 'Laporan Tindak Kekerasan',
    'version' '1.0',
    'summary' 'Modul untuk melaporkan tindak kekerasan',
    'description' 'Modul ini memungkinkan pengguna untuk melaporkan tindak kekerasan.',
    'author' 'Tristan',
    'depends' ['base'],
    'data' [
        'views/violence_report_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable' True,
    'application' True,
}