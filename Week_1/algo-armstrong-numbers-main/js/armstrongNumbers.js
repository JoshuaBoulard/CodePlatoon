function armstrong(arr) {
    let answer = [];
    let list = []
    for (let i = 0; i < arr.length; i++) {
        let count = arr[i].toString().length;
        let splitNum = arr[i].toString().split('');
        let nums = 0;

        for (let j = 0; j < splitNum.length; j++) {
            let powers = Number(splitNum[j])**Number(count)
            nums += powers
    
        }
        list.push(nums)
        if (arr[i] == nums) {
            answer.push(arr[i])
            console.log(answer)
        }
        
    }
}
console.log(armstrong([371,40,50]))
