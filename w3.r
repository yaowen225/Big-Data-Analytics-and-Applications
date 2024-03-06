xbar <- c(1000)
n <- 500
sample_size <- 5

for (i in 1:n) {
  x <- runif(sample_size)
  xbar[i] <- sum(x) / sample_size
}

hist(xbar)
