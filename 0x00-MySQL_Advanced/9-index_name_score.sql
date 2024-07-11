-- Creates an index 'index_name_first_score' on the 'names' table and the first
-- letter of 'name' and the 'score'.
CREATE INDEX index_name_first_score ON names (name(1), score);
