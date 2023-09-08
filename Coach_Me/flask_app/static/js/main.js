// Load the selected role from Local Storage on page load
window.addEventListener('load', function() {
    var selectedOption = localStorage.getItem('selectedRole');
    if (selectedOption) {
        var selectElement = document.getElementsByName("role")[0];
        selectElement.value = selectedOption;
        user_user_measures();
    }
});

// Save the selected role to Local Storage when the selection changes
function user_user_measures() {
    var selectedOption = document.getElementsByName("role")[0];
    var allDivs = document.querySelectorAll(".hidden");
    var hiddenFile = document.getElementById("hidden_file");

    for (var i = 0; i < allDivs.length; i++) {
        allDivs[i].style.display = "none";
    }

    if (selectedOption.value === "u") 
    {
        for (var i = 0; i < allDivs.length; i++) {
            allDivs[i].style.display = "block";
        }
        hiddenFile.style.display = "block";
    } 
    else if (selectedOption.value === "c")
    {
        hiddenFile.style.display = "block";
        for (var i = 0; i < allDivs.length; i++) {
            allDivs[i].style.display = "none";
        }
    }
    else
    {
        hiddenFile.style.display = "none";
        for (var i = 0; i < allDivs.length; i++) {
            allDivs[i].style.display = "none";
        }
    }

    localStorage.setItem('selectedRole', selectedOption.value);
}

function toggleInput(checkbox, inputId) {
    const input = document.getElementById(inputId);
    if (checkbox.checked) {
        input.disabled = true;
        input.value = ''; 
    } else {
        input.disabled = false;
    }
}

function toggleInput_for_update(checkbox, inputId) {
    const input = document.getElementById(inputId);
    if (checkbox.checked) {
        input.style.pointerEvents = 'none';
        
    } else {
        input.style.pointerEvents = 'auto';
        input.focus()
    }
}

function updateProfilePicture(input) {
    const file = input.files[0];
    const profilePicture = document.getElementById('profilePicture');
    const reader = new FileReader();

    reader.onload = function (e) {
        profilePicture.src = e.target.result;
    };

    reader.readAsDataURL(file);
}
