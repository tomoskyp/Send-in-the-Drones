h1 <- cbind(-65.65, 18.33)
h2 <- cbind(-66.03, 18.22)

library(geosphere)
steps = seq(0, 360, 0.1)
c1 <- destPoint(p1, steps, 107.5 * 1852)
c2 <- destPoint(p2, steps, 145 * 1852)

library(raster)
s1 <- spLines(c1)
s2 <- spLines(c2)

i <- intersect(s1, s2)
coordinates(i)

#        x        y
# -92.38241 38.24267
# -88.15830 36.98740

s <- bind(s1, s2)
crs(s) <- "+proj=longlat +datum=WGS84"
plot(s)
points(i, col='red', pch=20, cex=2)