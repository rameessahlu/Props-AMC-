function form_submit(myForm) {
  console.log("form submit is working!"); // sanity check
  var formUrl = $("#form_url").data().name;
  console.log($("#file-name").val());
  console.log($("#excel-file").val());
  console.log(formUrl);

  var formData = new FormData(myForm);

  $.ajax({
    contentType: false,
    processData: false,
    type: "POST",
    url: formUrl,
    data: formData,
    success: function (table_html) {
      // removing value from the input fields
      $("#file-name").val("");
      $("#excel-file").val("");

      //console.log(table_html);
      $("#add-book-table").empty();
      $("#add-book-table").prepend(table_html);

      document.getElementById("submit").disabled = false;
      $("#submit-success-alert").show("fade");
      console.log("success"); // another sanity check

      setTimeout(function () {
        $("#submit-success-alert").hide("fade");
      }, 2000);
    },

    // handle a non-successful response
    error: function (xhr, errmsg, err) {
      $("#submit-fail-alert").show("fade");
      setTimeout(function () {
        $("#submit-fail-alert").hide("fade");
      }, 2000);
      document.getElementById("submit").disabled = false;
    },
  });
}
