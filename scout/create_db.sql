PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE searches (id INTEGER PRIMARY KEY, site_url TEXT, trim_begin TEXT, trim_end TEXT, re_title TEXT, re_date TEXT, re_id TEXT, re_description TEXT, description TEXT);
CREATE TABLE posts (id INTEGER PRIMARY KEY, title TEXT, date TEXT, description TEXT);
CREATE TABLE search_terms (id INTEGER PRIMARY KEY, term TEXT);

INSERT INTO searches (site_url, trim_begin, trim_end, re_title, re_date, re_id, re_description, description) VALUES (
    'http://www.ls1gto.com/forums/forumdisplay.php?f=19',
    '<!-- show threads -->',
    '<!-- end show threads -->',
    'e_[0-9]*">.*<',
    '[0-9TY].*time.*M',
    'n_[0-9]*">',
    '_[0-9]*" t.*?">',
    'LS1GTO.com For Sale forum');

INSERT INTO search_terms (term) VALUES ('drag');
INSERT INTO search_terms (term) VALUES ('radial');
INSERT INTO search_terms (term) VALUES ('wheel');
INSERT INTO search_terms (term) VALUES ('tire');
INSERT INTO search_terms (term) VALUES ('exhaust');
INSERT INTO search_terms (term) VALUES ('cat');
INSERT INTO search_terms (term) VALUES ('pipe');
INSERT INTO search_terms (term) VALUES ('coil');
INSERT INTO search_terms (term) VALUES ('spring');
INSERT INTO search_terms (term) VALUES ('rim');
INSERT INTO search_terms (term) VALUES ('sub');
INSERT INTO search_terms (term) VALUES ('shifter');

COMMIT;
