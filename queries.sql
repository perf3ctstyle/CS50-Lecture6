CREATE TABLE favorites
(
    title TEXT,
    genre TEXT
);

SELECT * FROM favorites;
SELECT genre FROM favorites;
SELECT COUNT(*) AS counter FROM favorites WHERE genre = 'Adventure';

CREATE TABLE show
(
    id INTEGER,
    title TEXT NOT NULL,
    PRIMARY KEY(id)
);
CREATE TABLE genre
(
    show_id INTEGER,
    genre TEXT NOT NULL,
    FOREIGN KEY(show_id) REFERENCES show(id)
);

SELECT DISTINCT title FROM show WHERE id IN (SELECT show_id FROM genre WHERE genre = 'Comedy');
SELECT DISTINCT title FROM show WHERE id IN (SELECT show_id FROM genre WHERE genre = 'Comedy') ORDER BY title;

INSERT INTO show VALUES("Seinfeld");
INSERT INTO genre(show_id, genre) VALUES(1, 'Comedy');
UPDATE show SET title = 'SEINFELD' WHERE title = 'Seinfeld';

CREATE INDEX title_index ON show(title);

CREATE TABLE person
(
    id INTEGER,
    name TEXT NOT NULL,
    birth NUMERIC,
    PRIMARY KEY(id)
);
CREATE TABLE stars
(
    show_id INTEGER,
    person_id INTEGER,
    FOREIGN KEY(show_id) REFERENCES show(id),
    FOREIGN KEY(person_id) REFERENCES person(id)
);

SELECT show_id FROM stars WHERE person_id = (SELECT id FROM person WHERE name = 'Steve Carell');
SELECT title FROM show WHERE id IN
                             (SELECT show_id FROM stars WHERE person_id =
                                                              (SELECT id FROM person WHERE name = 'Steve Carell'));

CREATE INDEX show_index ON stars(show_id);
CREATE INDEX person_index ON stars(person_id);
CREATE INDEX name_index ON person(name);

SELECT title FROM person JOIN stars on person.id = stars.person_id JOIN show on stars.show_id = show.id;
SELECT title FROM person, stars, show
                                    WHERE person.id = stars.person_id
                                    AND stars.show_id = show.id
                                    AND person.name = 'Steve Carell';