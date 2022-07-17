-- upgrade --
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "first" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_time" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(40) NOT NULL
);
CREATE TABLE IF NOT EXISTS "second" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_time" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(40) NOT NULL
);
