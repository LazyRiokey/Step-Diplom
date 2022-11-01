// /**
// Создаем intersection observer
// elem - элемент для «наблюдения»
// callback - callback-функция
// options - объект опций, если они необходимы (необязательный параметр)
// */
// function createIntersectionObserver (elem, callback, options) {
//     let observer = new IntersectionObserver(callback, options || {});
//     observer.observe(document.querySelector(".first-page-container"));
//     return observer;
// }

// /**
// Выводим в консоль элемент, если он входит в зону видимости
// entries - массив «наблюдаемых» элементов
//  */
// function log (entries) {
//     let [entry] = entries;
//     console.log(entries);
//     console.log(entry.target);
//     console.log(entry.isIntersecting);
// }

// // Задаем опции для «наблюдателя»
// let options = {
//     rootMargin: '50px'
// };

// // Указываем элементы для «наблюдения»
// let el_1 = document.querySelector('.first-flexbox');
// // let el_2 = document.querySelector('.element_2');

// /**
// Создаем «наблюдателя» для каждого элемента
// Для первого указываем опции
// */
// createIntersectionObserver(el_1, log, options);

// // Второй использует ту же самую callback-функцию, но без опций
// // createIntersectionObserver(el_2, log);