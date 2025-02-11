
const taskInput = document.getElementById("taskInput");
const addTaskBtn = document.getElementById("addTaskBtn");
const taskList = document.getElementById("taskList");

// Load tasks from localStorage
function loadTasks() {
    const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    taskList.innerHTML = "";
    tasks.forEach((task, index) => addTaskToDOM(task, index));
}

// Add a new task
function addTask() {
    const taskText = taskInput.value.trim();
    if (taskText === "") {
        alert("Task cannot be empty!");
        return;
    }
    
    const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.push(taskText);
    localStorage.setItem("tasks", JSON.stringify(tasks));
    addTaskToDOM(taskText, tasks.length - 1);
    taskInput.value = "";
}

// Add task to DOM
function addTaskToDOM(task, index) {
    const li = document.createElement("li");
    li.innerHTML = `
        <span>${task}</span>
        <button onclick="editTask(${index})">Edit</button>
        <button onclick="deleteTask(${index})">Delete</button>
    `;
    taskList.appendChild(li);
}

// Edit a task
function editTask(index) {
    const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    const updatedTask = prompt("Edit task:", tasks[index]);
    if (updatedTask !== null && updatedTask.trim() !== "") {
        tasks[index] = updatedTask.trim();
        localStorage.setItem("tasks", JSON.stringify(tasks));
        loadTasks();
    }
}

// Delete a task
function deleteTask(index) {
    const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.splice(index, 1);
    localStorage.setItem("tasks", JSON.stringify(tasks));
    loadTasks();
}

// Event listener for adding task
addTaskBtn.addEventListener("click", addTask);

// Load tasks on page load
window.onload = loadTasks;
