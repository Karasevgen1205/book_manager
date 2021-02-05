// 1 Переменные

// camalCase

// // variable
// var name = 'Yauheni' // Устаревшая и глобальная
// const lastName = 'Karas'
// const isProgrammer = true // boolean
// let age = 26 // number
// const _private = 'private'
// const _$private = 'private'
// const withNum5 = 5

// name = 'Yauhen'
// age = 29

// console.log(name)

// // 2 Мутирование

// console.log('Имя человека: ' + name + ' , а возраст человека: ' + age)
// console.log(age)
// console.log(age.toString())

// //alert('Are you sure?')

// const firstName = prompt('Entry you name') // Окно ввода по типу alert
// alert(firstName + ' ' + lastName)

// // 3 Операторы

// let currentYear = 2020
// let birthYear = 1991

// let fullAge = currentYear - birthYear
// console.log(fullAge)

// const a = 10
// const b = 5
// let c = 32

// console.log(a - b)
// console.log(a + b)
// console.log(a / b)
// console.log(a * b)
// console.log(currentYear++) // ++ добавляет при следуюещм вызове 1 (можно в начале или в конце)
// console.log(currentYear--) // -- отнимает при следуюещм вызове 1 (можно в начале или в конце)
// console.log(currentYear)

// c = c + a
// c += a
// c -= a
// c /= a
// c *= a

// 4 Типы данных

// const isProgrammer = true
// const name = 'Yauheni'
// const age = 26
// let x
// null

// console.log(typeof isProgrammer)
// console.log(typeof name)
// console.log(typeof age)
// console.log(typeof x)
// console.log(typeof null)


// 5 Приоритет операторов

// const fullAge = 29
// const birthYear = 1991
// const currentYear = 2021

// const isFullAge = currentYear - birthYear >= fullAge // 29 >= 30 > true
// console.log(isFullAge)

// 6 Условные операторы

// const courseStatus = 'pending' // 'ready', 'fail'

// if (courseStatus === 'pending') {
//     console.log('Курс находится в стадии разрабокти')
// } else if (courseStatus === 'ready') {
//     console.log('Курс уже готов')
// } else {
//     console.log('Pull Shet!')
// }

// Работа с IF с типом данных Boolean

// const isReady = true

// if (isReady) {
//     console.log('Ok')
// } else {
//     console.log('Fuck')
// }

// Тернарное выражение (альтернатива привычному IF ELSE):
// isReady ? console.log('Ok') : console.log('Fuck')

// Особенность работы с == и ===

// const num1 = 42 // number
// const num2 = '42' // string

// console.log(num1 == num2) // true
// console.log(num1 === num2) // false

// 7 Булевая логика

// AND
// true && true  // true
// true && false // false
// false && true // false
// false && false // false

// OR
// true || true  // true
// true || false // true
// false || true // true
// false || false // false

// 8 Функции

// function calculateAge(year){
//     return 2021 - year
// }

// const myAge = calculateAge(1991)
// console.log(myAge)

// console.log(calculateAge(1991))
// console.log(calculateAge(1999))
// console.log(calculateAge(2000))
//
// function logInfoAbout(name, year){
//     const age = calculateAge(year)
//
//     if (age > 0){
//         console.log('Human ' + name + ' have age ' + age)
//     } else {
//         console.log('This is unable')
//     }
// }

// logInfoAbout('Yauheni', 1991)
// logInfoAbout('Yauheni', 2263)

// 9 Массивы
// const cars = new Array('Mazda', 'Audi', 'BMW') // Not good!
// OR
const cars = ['Mazda', 'Audi', 'BMW'] // Very good!
console.log(cars)

console.log(cars[0])
console.log(cars[1])
console.log(cars[3])
console.log(cars[2])
console.log(cars.length)

cars[0] = 'Porsche' // добавление на позицию "0"
cars[3] = 'LADA' // добавление на позицию "3"
cars[cars.length] = 'Lambo' // добавление в конец списка
console.log(cars)



