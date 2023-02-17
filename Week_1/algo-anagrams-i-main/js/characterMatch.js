function characterMatch(string1, string2) {
  let s1 = string1.toUpperCase().split('').sort().join('')
  let s2 = string2.toUpperCase().split('').sort().join('')
  if (s1 === s2) {
    return true 
  } 
  return false


};

//console.log(characterMatch('charm', 'mrch'))

function charMatchArr(arr) {
let compare = []
let answer = []
let count = 0
let fin = []
   for (let x of arr) {
     compare.push(x.toUpperCase().split('').sort().join(''))
   }
   while (count < arr.length) {
    let formula = compare.shift()
     for (let i = 0; i < compare.length; i++) {
        if (compare[i] === formula) {
            answer.push(count)
            break
        }
     }
     compare.push(formula)
     count++
   }
    
   for (let j = 0; j < answer.length; j++) {
     fin.push(arr[answer[j]])
   }

   return fin
}

console.log(charMatchArr(["cognac", "saltier", "realist", "retails"]))