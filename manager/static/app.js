// 1 Переменные

// camalCase

// variable
var name = 'Yauheni' // Устаревшая и глобальная
const lastName = 'Karas'
const isProgrammer = true // boolean
let age = 26 // number
const _private = 'private'
const _$private = 'private'
const withNum5 = 5

name = 'Yauhen'
age = 29

console.log(name)

// 2 Мутирование

console.log('Имя человека: ' + name + ' , а возраст человека: ' + age)
console.log(age)
console.log(age.toString())

//alert('Are you sure?')

const firstName = prompt('Entry you name') // Окно ввода по типу alert
alert(firstName + ' ' + lastName)

// 3 Операторы

let currentYear = 2020
let birthYear = 1991

let fullAge = currentYear - birthYear
console.log(fullAge)

const a = 10
const b = 5
let c = 32

console.log(a - b)
console.log(a + b)
console.log(a / b)
console.log(a * b)
console.log(currentYear++) // ++ добавляет при следуюещм вызове 1 (можно в начале или в конце)
console.log(currentYear--) // -- отнимает при следуюещм вызове 1 (можно в начале или в конце)
console.log(currentYear)

c = c + a
c += a
c -= a
c /= a
c *= a

// 4 Типы данных



