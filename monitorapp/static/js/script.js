//:user interface
$(document).ready(function(){
  $("#form").click(function(){
    $("#test").hide();
  });
});

$(document).ready(function() {
    $(".create-review").modalForm({
        formURL: "{% url 'newreview' %}"
    });
});
