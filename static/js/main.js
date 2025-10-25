// Generate stars
const starsContainer = document.getElementById('stars');
const starCount = 180;
for (let i = 0; i < starCount; i++) {
    const star = document.createElement('div');
    const size = Math.random() > 0.92 ? 'large' : Math.random() > 0.65 ? 'medium' : 'small';
    star.className = `star ${size}`;
    star.style.left = `${Math.random() * 100}%`;
    star.style.top = `${Math.random() * 100}%`;
    star.style.animationDelay = `${Math.random() * 3}s`;
    star.style.animationDuration = `${2.5 + Math.random() * 2}s`;
    starsContainer.appendChild(star);
}

function addTaskInput() {
    const taskList = document.getElementById('task-list');
    const newInput = document.createElement('input');
    newInput.type = 'text';
    newInput.name = 'tasks';
    newInput.placeholder = 'New Task';
    newInput.className = 'form-input task-input';
    taskList.appendChild(newInput);
}