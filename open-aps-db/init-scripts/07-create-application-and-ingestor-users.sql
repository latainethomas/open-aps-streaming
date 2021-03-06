\set ingestor_password `echo "$POSTGRES_INGESTOR_PASSWORD"`
\set admin_viewer_password `echo "$POSTGRES_ADMIN_VIEWER_PASSWORD"`
\set viewer_password `echo "$POSTGRES_VIEWER_PASSWORD"`
\set ext_openaps_app_password `echo "$POSTGRES_EXT_OPENAPS_APP_PASSWORD"`
\set register_user `echo "$POSTGRES_REGISTER_USER"`

CREATE USER ingestor;
GRANT ingestor to open_aps_admin;
ALTER USER ingestor WITH ENCRYPTED PASSWORD :'ingestor_password';
GRANT USAGE ON SCHEMA openaps TO ingestor;
ALTER ROLE ingestor SET search_path = 'openaps';
GRANT ALL ON schema openaps TO ingestor;
ALTER DEFAULT PRIVILEGES IN schema openaps GRANT UPDATE, INSERT, SELECT, DELETE ON TABLES TO ingestor;
GRANT USAGE ON SCHEMA register TO ingestor;
GRANT ALL ON schema register TO ingestor;
ALTER DEFAULT PRIVILEGES FOR USER :register_user IN schema register GRANT SELECT ON TABLES TO ingestor;
ALTER DEFAULT PRIVILEGES FOR USER :register_user IN schema register GRANT SELECT ON SEQUENCES TO ingestor;

CREATE USER admin_viewer;
GRANT admin_viewer to open_aps_admin;
ALTER USER admin_viewer WITH ENCRYPTED PASSWORD :'admin_viewer_password';
GRANT USAGE ON SCHEMA openaps TO admin_viewer;
GRANT SELECT ON ALL TABLES IN SCHEMA openaps TO admin_viewer;
ALTER DEFAULT PRIVILEGES IN schema openaps GRANT SELECT ON TABLES TO admin_viewer;

CREATE USER viewer;
GRANT viewer to open_aps_admin;
ALTER USER viewer WITH ENCRYPTED PASSWORD :'viewer_password';
GRANT USAGE ON SCHEMA openaps TO viewer;
ALTER DEFAULT PRIVILEGES IN schema openaps GRANT SELECT ON TABLES TO viewer;
ALTER DEFAULT PRIVILEGES IN schema openaps GRANT SELECT ON SEQUENCES TO viewer;

CREATE USER ext_openaps_app;
GRANT ext_openaps_app to open_aps_admin;
ALTER USER ext_openaps_app WITH ENCRYPTED PASSWORD :'ext_openaps_app_password';
GRANT USAGE ON SCHEMA openaps TO ext_openaps_app;


