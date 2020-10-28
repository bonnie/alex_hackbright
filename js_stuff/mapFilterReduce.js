Welcome to Node.js v14.13.1.
Type ".help" for more information.
> x = [1, 3, 5]
[ 1, 3, 5 ]
> x.map(num => num * 2)
[ 2, 6, 10 ]
> x = [1, 3, 5]
[ 1, 3, 5 ]
> x.filter(x => x > 2)
[ 3, 5 ]
> x.reduce((total, num) => total + num, 0)
9
> st = ['a', 'b', 'c']
[ 'a', 'b', 'c' ]
> st.reduce((finalString, s) => finalString + s, 'My favorite letters are ')
'My favorite letters are abc'


Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> x = [1, 3, 5]
>>> map(lambda num: num*2, x)
<map object at 0x109164ac0>
>>> list(map(lambda num: num*2, x))
[2, 6, 10]
>>> [ num * 2 for num in x]
[2, 6, 10]
