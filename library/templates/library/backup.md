## index.html

    <h1 class="w3-text-teal">Biblioteca Personal</h1>
    <p>Bienvenido a esta página de gestion de bibliotecas, esta es la página principal de la biblioteca personal.
        En la parte superior de la página, puedes acceder a las opciones de búsqueda de libros, visualizar tu perfil personal, o crear el tuyo propio con la opción de registro.
        A continuación podrás ver libros seleccionados aleatoriamente, de los disponibles en la biblioteca.
    </p>

    <h2 class="w3-text-purple">N° {{ primer_id }}. {{ primero }}</h2>
        <h3>Descripción:</h3>
        <p>{{ primero_description }}</p>
    <a href="/libro/{{ primer_id }}">Ver detalles del libro.</a>

    <h2 class="w3-text-purple">N° {{ segundo_id }}. {{ segundo }}</h2>
        <h3>Descripción: </h3>
        <p>{{ segundo_description }}</p>
    <a href="/libro/{{ segundo_id}}">Ver detalles del libro.</a>

    <a href="/buscar" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Buscar</a>
    <a href="/perfil" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Perfil</a>
    <a href="/registrar" class="w3-bar-item w3-theme-l1 w3-button w3-right">Registrarse</a>

## book.html

      <h1 class="w3-text-teal">Libro N° {{ id }}</h1>
        <h3 class="w3-text-teal">Título: {{ title }}</h3>
        <h4> Descripción: </h4>
        <p>{{ description }}</p>
        <p> Este libro contiene: {{ pages }} páginas.</p>

## search.html

    <a href="/" class="w3-bar-item w3-button w3-theme-l1">Biblioteca</a>
    <a href="/buscar" class="w3-bar-item w3-hover-white">Buscar</a>
    <a href="/perfil" class="w3-bar-item  w3-hover-white">Perfil</a>
    <a href="/registrar" class="w3-bar-item w3-theme-l1 w3-button w3-right">Registrarse</a>

    <h1 class="w3-text-teal">Buscador</h1>
    <p>
        En esta página, podrás buscar libros según su nombre, autor o descripción.
    </p>
    <p>
        Ingresa tu búsqueda en el barra inferior.
        (cuidado con la ortografía).

    <form action="{% url 'search_page' %}" method="get">
        <input type="search" id="buscador" name="q" placeholder="Ingresa título o autor...">
        <!-- <input type="submit" value="Buscar!"> -->
    </form>

    <div class="w3-container w3-padding-32">
    <h2 class="w3-border-bottom w3-border-light-grey">Resultados de búsqueda: </h2>
    </div>

    <div class="w3-row-padding w3-grayscale">
    
    {% for book in object_list %}
        <div class="w3-col m6 w3-margin-bottom ">
        <h3>{{ book.title }}</h3>
        <p class="w3-opacity"> {{ book.author }}</p>
        <a href="/libro/{{ book.id }}">Ver detalles del libro.</a>
        </div>  
    {% endfor %}
    </div>









         