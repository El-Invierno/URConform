s = r"""
\documentclass[11pt, a4paper]{article}
\usepackage{graphicx} % Required for inserting images
\usepackage{amsfonts,amsmath,amssymb}
\usepackage{float}
\usepackage{enumerate}
\parindent 0px
\usepackage{hyperref}
\usepackage{fullpage}

\begin{document}

% UR Header & Logo.
\noindent
\begin{minipage}{0.2\textwidth}
    \includegraphics[width=2cm]{../data/template/image.png}
\end{minipage}
\hfill
\begin{minipage}{0.75\textwidth}
    \centering
    {\Large \textbf{Yash Tawde}}\\[0.3em]
    \small
    \begin{minipage}{0.45\textwidth}
        \centering
        Email: \href{mailto:john.doe@example.com}{john.doe@example.com}
    \end{minipage}
    \hfill
    \begin{minipage}{0.45\textwidth}
        \centering
        Mobile: +91-7715962004
    \end{minipage}\\
    Links: \url{https://www.linkedin.com/in/johndoe}, \url{https://portfolio-website.com}
\end{minipage}

% Horizontal line.
\vspace{1em}
\noindent \rule{\textwidth}{0.4pt}

% Professional Summary.
\section*{Professional Summary}
Data engineer with over 8+ years of experience specializing in data migration projects using \textbf{Databricks, Azure}, and \textbf{PySpark}. Strong technical skills in data migration and engineering with a proven track record in delivering large-scale projects. Proficient in team collaboration and project execution under tight deadlines.

% Horizontal line.
\vspace{1em}
\noindent \rule{\textwidth}{0.4pt}

% Tools and Technology.
\section*{Tools \& Technologies}
\begin{table}[H]
    \centering
    \begin{tabular}{|p{5cm}|p{5cm}|}
        \hline
        \textbf{Category} & \textbf{Tools / Technologies} \\
        \hline
        Databases & MS SQL Server \\
        \hline
        Programming & Python, PySpark, Spark, Hive, Azure DevOps, SQL, U-SQL, Oracle, NoSQL (Cosmos DB) \\
        \hline
        Data Integration \& ETL & Azure Data Factory \\
        \hline
        Issue Tracking \& Project Management & JIRA \\
        \hline
        Visualization Tools & Power BI \\
        \hline
        Cloud Data & Databricks, Azure Data Lake, Azure Synapse \\
        \hline
    \end{tabular}
\end{table}

% Horizontal line.
\vspace{1em}
\noindent \rule{\textwidth}{0.4pt}

% Professional Experience
\section*{Professional Experience}
% Role1, Company 1 [Duration]
\textbf{Senior Data Engineer, \small{\MakeUppercase{takeda innovations india pvt ltd}}}\\
\small{\small{\MakeUppercase{feb 2024 - present}}}\\[0.8em]
% Projects:
\underline{\large{Project: LVP}}
\begin{itemize}
    \item Optimized Databricks workloads using deletion vectors, partition pruning, spot VMs, and cluster optimization, achieving cost savings of 50\%.
    \item Migrated Hive Metastore to Unity Catalog for better data management and governance.
    \item Created an ACL framework in Unity Catalog to enable granular access control at the table, row, and column levels.
    \item Designed and implemented metadata-driven pipelines for extraction and orchestration in data factory, leveraged for building data products.
    \item Developed PySpark notebooks for streamlined data loading into bronze, silver, and gold tiers.
    \item Implemented access management in Databricks using PowerShell for clusters, SQL warehouses, and global job scripts.
    \item Developed data quality metrics ensuring completeness, uniqueness, accuracy, and timeliness of data.
    \item Constructed PySpark transformation reusable methods for streaming data processing tasks.
\end{itemize}

\vspace{0.5em}

\underline{\large{Project: SRP}}
\begin{itemize}
    \item Optimized Databricks workloads using deletion vectors, partition pruning, spot VMs, and cluster optimization, achieving cost savings of 50\%.
    \item Migrated Hive Metastore to Unity Catalog for better data management and governance.
    \item Created an ACL framework in Unity Catalog to enable granular access control at the table, row, and column levels.
    \item Designed and implemented metadata-driven pipelines for extraction and orchestration in data factory, leveraged for building data products.
    \item Developed PySpark notebooks for streamlined data loading into bronze, silver, and gold tiers.
    \item Implemented access management in Databricks using PowerShell for clusters, SQL warehouses, and global job scripts.
    \item Developed data quality metrics ensuring completeness, uniqueness, accuracy, and timeliness of data.
    \item Constructed PySpark transformation reusable methods for streaming data processing tasks.
\end{itemize}

\vspace{0.7em}

% Role2, Company 2 [Duration]
\textbf{\large{Senior Data Engineer}, \small{\MakeUppercase{graymatter software services pvt ltd}}}\\
\small{\small{\MakeUppercase{feb 2024 - present}}}\\[0.8em]
% Projects:
\underline{\large{Project: LVP}}
\begin{itemize}
    \item Optimized Databricks workloads using deletion vectors, partition pruning, spot VMs, and cluster optimization, achieving cost savings of 50\%.
    \item Migrated Hive Metastore to Unity Catalog for better data management and governance.
    \item Created an ACL framework in Unity Catalog to enable granular access control at the table, row, and column levels.
    \item Designed and implemented metadata-driven pipelines for extraction and orchestration in data factory, leveraged for building data products.
    \item Developed PySpark notebooks for streamlined data loading into bronze, silver, and gold tiers.
    \item Implemented access management in Databricks using PowerShell for clusters, SQL warehouses, and global job scripts.
    \item Developed data quality metrics ensuring completeness, uniqueness, accuracy, and timeliness of data.
    \item Constructed PySpark transformation reusable methods for streaming data processing tasks.
\end{itemize}

\vspace{0.5em}

\underline{\large{Project: SRP}}
\begin{itemize}
    \item Optimized Databricks workloads using deletion vectors, partition pruning, spot VMs, and cluster optimization, achieving cost savings of 50\%.
    \item Migrated Hive Metastore to Unity Catalog for better data management and governance.
    \item Created an ACL framework in Unity Catalog to enable granular access control at the table, row, and column levels.
    \item Designed and implemented metadata-driven pipelines for extraction and orchestration in data factory, leveraged for building data products.
    \item Developed PySpark notebooks for streamlined data loading into bronze, silver, and gold tiers.
    \item Implemented access management in Databricks using PowerShell for clusters, SQL warehouses, and global job scripts.
    \item Developed data quality metrics ensuring completeness, uniqueness, accuracy, and timeliness of data.
    \item Constructed PySpark transformation reusable methods for streaming data processing tasks.
\end{itemize}

% Horizontal line.
\vspace{1em}
\noindent \rule{\textwidth}{0.4pt}

% Certifications
\section*{Certifications}
\textbf{
\begin{itemize}
    \item Google Data Science Certification
    \item Amazon Web Service Architect
    \item Joomla Data Analyst Bootcamp
\end{itemize}
}

% Horizontal line.
\vspace{1em}
\noindent \rule{\textwidth}{0.4pt}

% Education
\section*{Education}
\begin{table}[H]
    \centering
    \begin{tabular}{|p{3cm}|p{3cm}|p{3cm}|}
        \hline
        Year & Degree & Institution\\
        \hline
        2009 & BTEch & Biju Pattnaik University of Technology, Bhubaneshwar\\
        \hline
        2009 & 12th & Kendriya Vidyalaya\\
        \hline
    \end{tabular}
\end{table}

\end{document}
"""