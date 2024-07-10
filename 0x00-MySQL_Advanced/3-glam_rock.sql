-- Lists all bands with Glam Rock as their main style, ranked by longevity
SELECT band_name, IFNULL(split, 2022) - formed as lifespan
FROM metal_bands
ORDER BY lifespan DESC;