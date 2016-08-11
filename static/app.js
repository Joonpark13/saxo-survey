$(function() {
    $("#submit-button").click(function() {
        aggregate_text = "";

        // Add static questions
        $("#question-list").children('li').each(function() {
            aggregate_text += "<p>" + $(this).children('p').first().html();
            aggregate_text += $(this).children('textarea').first().val() + "</p>";
        });

        // Add custom question
        aggregate_text += "<p>" + $("#make-up-question").val() + " " +  $("#make-up-answer").val() + "</p>";

        $("#copy-paste").html(
            "<h4 id='copy-paste-instruction'>Copy and paste the text below as a reply to the survey email thread!</h4>" +
            "<br>" +
            aggregate_text +
            "<br>" +
            "Go to " + window.location.href + " to continue the survey!"
        );

        // Show the instruction so the user will notice.
        document.getElementById("copy-paste-instruction").scrollIntoView();
    });
});