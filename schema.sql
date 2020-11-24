CREATE TABLE IF NOT EXISTS ratings (
    film_id varchar(255),
    user_id varchar(255),
    rating int(11),
    PRIMARY KEY (film_id, user_id)
);

