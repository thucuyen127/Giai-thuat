
library("igraph")
library("scales")
library("graphsim")

vo_huong <- make_graph( ~ A-B-C-D-E-A, G-A:B:C:D:E)
plot(vo_huong)
