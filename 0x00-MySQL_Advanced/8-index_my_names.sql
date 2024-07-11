-- Creates an index 'index_name_first' on the table 'names' and the first letter of name
CREATE INDEX index_name_first ON names (name(1));
