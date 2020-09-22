document.addEventListener('DOMContentLoaded', function() {
    document.querySelector("#id_search_form").onsubmit = () => {
        if (document.querySelector("#id_search_query").value == "") {
            return false;
        }
    }

    document.querySelector(".class_new_article").onclick = () => {
        document.querySelector("#id_article_body").style.display = "none";
        document.querySelector("#id_new_article_form").style.display = "block";
        return false;
    }

    document.querySelector(".class_search_article").onclick = () => {
        document.querySelector("#id_search_query").value = document.title;
        document.querySelector("#id_search_form").submit();
    }
});