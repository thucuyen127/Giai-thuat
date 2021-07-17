ucln <- function(x, y) {
  while(y) {
    temp = y
    y = x %% y
    x = temp
  }
  return(x)
}
ucln(6,9)
