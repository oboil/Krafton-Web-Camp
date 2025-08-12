let b_list = [4, 1, 0];
a_list.push(b_list);
a_list; // [1, 4, 2, [3, 1], [4, 1, 0]]
a_list.length; // 5

// 리스트와 리스트를 이어붙이고 싶다면
let c_list = a_list.concat(b_list);
c_list; // [1, 4, 2, [3, 1], [4, 1, 0], 4, 1, 0]
a_list; // [1, 4, 2, [3, 1], [4, 1, 0]] 원본 리스트는 변하지 않아요

// push: 그거 자체를 넣음 (리스트면 리스트, 딕셔너리면 딕셔너리). 원본 변경 o
// concat: 요소를 이어 붙임. 원본 변경 x
