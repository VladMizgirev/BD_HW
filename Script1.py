
CREATE TABLE IF NOT EXISTS genres (
	genre_id INTEGER PRIMARY KEY,
	title VARCHAR(40) NOT null
	);

CREATE TABLE IF NOT EXISTS executor (
	executor_id INTEGER PRIMARY KEY,
	name_executor VARCHAR(40) NOT null
	);

CREATE TABLE IF NOT EXISTS albums (
	album_id INTEGER PRIMARY KEY,
	name_album VARCHAR(40) NOT null,
	year_of_release INTEGER NOT null
	);

CREATE TABLE IF NOT EXISTS tracks (
	track_id INTEGER PRIMARY kEY,
	album_id INTEGER NOT null,
	name_track VARCHAR(40) NOT null,
	year_of_release INTEGER NOT null,
	name_album VARCHAR(40) NOT null
	);

CREATE TABLE IF NOT EXISTS collections (
	collection_id INTEGER PRIMARY kEY,
	name_collection VARCHAR(40) NOT null,
	year_of_release INTEGER NOT null
	);

CREATE TABLE IF NOT EXISTS genre_executor (
	genre_id INTEGER REFERENCES genres(genre_id),
	executor_id INTEGER REFERENCES executor(executor_id),
	CONSTRAINT pk PRIMARY KEY (genre_id, executor_id)
	);

CREATE TABLE IF NOT EXISTS album_executor (
	album_id INTEGER REFERENCES albums (album_id),
	executor_id INTEGER REFERENCES executor(executor_id),
	CONSTRAINT pkae PRIMARY KEY (album_id, executor_id)
	);
	
CREATE TABLE IF NOT EXISTS track_collection (
	collection_id INTEGER REFERENCES collections (collection_id),
	track_id INTEGER REFERENCES tracks (track_id),
	CONSTRAINT pktc PRIMARY KEY (track_id, collection_id)
	);