const express = require("express");

const app = express();

app.get("/", function (req, res) {
    return res.send(
        "<h1>Hello</h1>"
    );
});

app.listen(process.env.PORT || 7000, () => {
    console.log("Server is running");
});