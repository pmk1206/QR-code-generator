<%--
    Document   : add
    Created on : Oct 9, 2026, 10:00:00 AM
    Author     : student
--%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Result</title>
    </head>
    <body>
        <h1>Result</h1>
        <%
            int a = Integer.parseInt(request.getParameter("n1"));
            int b = Integer.parseInt(request.getParameter("n2"));
        %>
        <p>
            <%= a %> + <%= b %> = <%= a + b %>
        </p>
        <a href="index.jsp">Back</a>
    </body>
</html>
