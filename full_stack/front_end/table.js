function addRow() {
    var table = document.getElementById('table');
    var length = table.rows.length;
    var new_row = table.insertRow(length);
    var nameCol = new_row.insertCell(0);
    var phoneCol = new_row.insertCell(1);
    var actionCol = new_row.insertCell(2);

    nameCol.innerHTML = '未命名';
    phoneCol.innerHTML = '无联系方式';
    actionCol.innerHTML = '<button onclick="editRow(this)">编辑</button> <button onclick="deleteRow(this)">删除</button>';
}

function deleteRow(button) {
    var row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
}

// 编辑数据函数 - 切换为输入状态
function editRow(button) {
    var row = button.parentNode.parentNode;
    var nameCell = row.cells[0];
    var phoneCell = row.cells[1];
    var actionCell = row.cells[2];

    // 获取当前单元格的值
    var currentName = nameCell.innerHTML;
    var currentPhone = phoneCell.innerHTML;

    // 将单元格内容替换为输入框
    nameCell.innerHTML = `<input type="text" value="${currentName}" class="edit-input">`;
    phoneCell.innerHTML = `<input type="text" value="${currentPhone}" class="edit-input">`;

    // 将编辑按钮替换为保存按钮
    actionCell.innerHTML = '<button onclick="saveRow(this)">保存</button> <button onclick="deleteRow(this)">删除</button>';

    // 自动聚焦到第一个输入框
    nameCell.querySelector('input').focus();
}

// 保存编辑内容函数
function saveRow(button) {
    var row = button.parentNode.parentNode;
    var nameCell = row.cells[0];
    var phoneCell = row.cells[1];
    var actionCell = row.cells[2];

    // 获取输入框的值
    var newName = nameCell.querySelector('input').value.trim();
    var newPhone = phoneCell.querySelector('input').value.trim();

    // 验证并设置默认值
    if (newName === "") {
        newName = "未命名";
    }
    if (newPhone === "") {
        newPhone = "无联系方式";
    }

    // 将输入框替换为文本内容
    nameCell.innerHTML = newName;
    phoneCell.innerHTML = newPhone;

    // 将保存按钮替换为编辑按钮
    actionCell.innerHTML = '<button onclick="editRow(this)">编辑</button> <button onclick="deleteRow(this)">删除</button>';
}