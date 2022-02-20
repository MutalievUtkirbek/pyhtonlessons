function getSum(a, b) {
  if (a === b) {
    return a;
  } else {
    var sum = 0;
    for (var i = a; i <= b; i++) {
      sum += i;
    }
    return sum;
  }
}
