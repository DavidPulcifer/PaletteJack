const form = document.querySelector("#form");
        form.addEventListener("submit", function(e){
            e.preventDefault();
            getColors();
        });

        function getColors() {
            const query = form.elements.query.value
            fetch("/palette", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: new URLSearchParams({
                    query: query
                })
            })
            .then((response) => response.json())
            .then(data => {
                const colors = data.colors;
                const container = document.querySelector('.container');                
                createColorBoxes(colors, container);
            })
        }

        function createColorBoxes(colors, parent) {
            const replaceCheck = document.getElementById('replace');
            if (replaceCheck.checked) {
                parent.innerHTML = "";
            }

            for(const color of colors) {
                const div = document.createElement('div');
                div.classList.add('color');
                div.style.backgroundColor = color;
                div.style.width = "100%";

                div.addEventListener('click', function() {
                    navigator.clipboard.writeText(color);
                })
                
                div.addEventListener('contextmenu', function (event) {
                    event.preventDefault(); // Prevent the default right-click menu
                    div.remove(); // Remove the div from the DOM
                });

                const span = document.createElement('span');
                span.innerText = color
                div.appendChild(span);
                parent.appendChild(div);
            }
        }