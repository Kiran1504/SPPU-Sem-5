<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0">
    <!-- Output HTML -->
    <xsl:output method="html" indent="yes"/>

    <!-- Template to match the root element (employees) -->
    <xsl:template match="/employees">
        <html>
            <head>
                <title>Employee List</title>
                <link rel="stylesheet" type="text/css" href="styles.css"/>
            </head>
            <body>
                <h1>Employee Information</h1>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Position</th>
                        <th>Department</th>
                        <th>Salary</th>
                        <th>Hire Date</th>
                    </tr>
                    <!-- Loop through each employee -->
                    <xsl:for-each select="employee">
                        <tr>
                            <td><xsl:value-of select="@id"/></td>
                            <td><xsl:value-of select="name"/></td>
                            <td><xsl:value-of select="position"/></td>
                            <td><xsl:value-of select="department"/></td>
                            <td><xsl:value-of select="salary"/></td>
                            <td><xsl:value-of select="hireDate"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
