function sumPairs(arr, sum) {
    let count = 0; 
    let answer = []
    while (count < arr.length) {
        let formula = arr.shift()
         for (let i = 0; i < arr.length; i++) {
            if (Number(arr[i]) + Number(formula) === sum) {     
                answer.push([arr[i], formula]) 
            }
         }
         count++
    }
    return answer
}

console.log(sumPairs([2,3,6,6,10,12], 12))