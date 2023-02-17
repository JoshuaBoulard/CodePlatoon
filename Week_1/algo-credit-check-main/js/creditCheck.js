exports.creditCheck = function(str) {
   let reversingArray = str.split('')
   let checkDigit = reversingArray.pop()
   let reversedArrayToString = reversingArray.reverse().join('')
   let timesTwoArr = []
   let addedAllFinishedNums = 0
   
   for (let i = 0; i < reversedArrayToString.length; i++) {
     if (i % 2 === 0) {
        let doubleDigitCheck = reversedArrayToString[i] * 2
            if (doubleDigitCheck > 9) {
            let numberToArray = doubleDigitCheck.toString().split('')
            let addedDoubleDigits = (Number(numberToArray[0]) + Number(numberToArray[1]))
            timesTwoArr.push(addedDoubleDigits)
          } else {
            timesTwoArr.push(doubleDigitCheck)
                 }
    } else {
        timesTwoArr.push(reversedArrayToString[i])
           }
   }
   
   for (let j = 0; j < timesTwoArr.length; j++) {
    let makingEverythingANumber = Number(timesTwoArr[j])
    addedAllFinishedNums += makingEverythingANumber
   }
   
let checkDigitCalculation = ((10 - (addedAllFinishedNums % 10)) % 10)
console.log(checkDigitCalculation)
   if (checkDigitCalculation == checkDigit) {
      return 'The number is valid!'
   } else {
      return 'The number is invalid!'
   }
}
