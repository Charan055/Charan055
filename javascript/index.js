function table(num) {
  console.log(`---${num} table---`);
  for (let i = 0; i < 10; i++) {
    //   console.log(num + "*" + (i + 1) + "=" + num * (i + 1));
    console.log(`${num}*${i + 1}=${num * (i + 1)}`);
  }
}
// table(55);

const table2 = (num) => {
  console.log(`---${num} table---`);
  for (let i = 0; i < 10; i++) {
    //   console.log(num + "*" + (i + 1) + "=" + num * (i + 1));
    console.log(`${num}*${i + 1}=${num * (i + 1)}`);
  }
};
// table2(44);

function even(num) {
  console.log("---even function---");
  if (num % 2 == 0) {
    console.log(num, "is even");
  } else {
    console.log(num, "is odd");
  }
}
even(32);
