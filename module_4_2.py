def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function() # ничего не выводит
inner_function() # горовит нет такой буквы в этом слове
#выводит в консоль принт, только без внешней функции