let input = document.getElementById('item'), // Input Value
    button = document.getElementById('add'), // Add Button
    ol = document.getElementById('list'), // Ordered List <ol>
    clear = document.getElementById('clear'), // Clear All Button
    search = document.getElementById('search'); // Search Input

const todoList = {
    /*toDoCount: () => {
        document.getElementById('count').innerHTML = `ToDo Count: ${ol.children.length}`;
    },*/
    add: () => {
        if(input.value === '') {
            alert('Please enter your skill');
        } else {
            if(input.value.length <= 20) {
                ol.innerHTML += `
                    <li class="toDoItem">
                        <a class="text">${input.value}</a>
                        <span class="edit">Edit</span>
                        <span class="remove">Remove</span>
                    </li>
                `;
                localStorage.toDoItems = ol.innerHTML;          
            } else {
                alert('Max Length is 20');
            }
        }
    
        input.value = '';
        /*todoList.toDoCount();*/
    },
    enterPress: e => {
        if(e.keyCode === 13) {
            todoList.add();
        }
    },
    removeToDo: e => {
        if(e.target.className === 'remove') {
            e.target.parentElement.remove();
            localStorage.toDoItems = ol.innerHTML;
        }
        /*todoList.toDoCount();*/
    },
    editToDo: e => {
        if(e.target.className === 'edit') {
            let text = prompt('Edit Text');
            if(text === '') {
                alert('Can\'t Edit With Empty Prompt');
            } else if(text === null) {
                return;
            } else {
                e.target.parentElement.children[0].textContent = text;
                localStorage.toDoItems = ol.innerHTML;
            }
        }
    },
    clearToDo: () => {
        while(ol.firstChild) {
            ol.removeChild(ol.lastChild);
            localStorage.toDoItems = ol.innerHTML;
        }
        /*todoList.toDoCount();*/
    },
    checkedToDo: e => {
        if(e.target.classList.contains('text')) {
            e.target.classList.toggle('checked');
        }
    },
    searchToDo: e => {
        let list = document.getElementsByClassName('toDoItem');
        let text = e.target.value.toLowerCase();
        
        for(let i = 0; i < list.length; i++) {
            if(list[i].children[0].textContent.toLowerCase().indexOf(text) != -1) {
                list[i].style.display = 'block';
            } else {
                list[i].style.display = 'none';
            }
        }
    }
};

if (localStorage.toDoItems) {
    ol.innerHTML = localStorage.toDoItems;
  }

/*todoList.toDoCount();*/
button.addEventListener('click', todoList.add);
input.addEventListener('keyup', todoList.enterPress);
ol.addEventListener('click', todoList.removeToDo);
ol.addEventListener('click', todoList.editToDo);
ol.addEventListener('click', todoList.checkedToDo);
clear.addEventListener('click', todoList.clearToDo);
search.addEventListener('keyup', todoList.searchToDo);