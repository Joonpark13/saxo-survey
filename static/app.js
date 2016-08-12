$(function() {
    $("#submit-button").click(function() {
        // For displaying nicely formatted results to the user so they can
        // copy and paste into email
        aggregate_text = "";
        // For storing into db
        user_data = {};

        // Add static questions
        $("#question-list").children('li').each(function() {
            var question_text = $(this).children('p').first().html();
            var answer_text = $(this).children('textarea').first().val();

            aggregate_text += "<p>" + question_text;
            aggregate_text += answer_text + "</p>";

            user_data[question_text] = answer_text;
        });

        // Add custom question
        custom_question = $("#make-up-question").val() + " ";
        custom_answer = $("#make-up-answer").val();
        aggregate_text += "<p>" + custom_question + custom_answer + "</p>";

        $("#copy-paste").html(
            "<h4 id='copy-paste-instruction'>Copy and paste the text below as a reply to the survey email thread!</h4>" +
            "<br>" +
            aggregate_text +
            "<br>" +
            "Go to " + window.location.href + " to continue the survey!"
        );

        // Show the instruction so the user will notice.
        document.getElementById("copy-paste-instruction").scrollIntoView();

        // Send data to server
        $.ajax({
            type: "POST",
            url: "/add",
            data: JSON.stringify({
                static: user_data,
                custom: {q: custom_question, a: custom_answer}
            }),
            //dataType: "json"
            contentType: "application/json"
        });
    });
});