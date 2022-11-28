# devpathsHomework5

Homework
a small service on the web that has two endpoints:

1. /messages takes a message (a string) as a POST and returns the SHA256 hash digest of that
message (in hexadecimal format)

2. /messages/<hash> is a GET request that returns the original message. A request to a non-existent
<hash> should return a 404 error.
