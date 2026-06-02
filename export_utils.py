import csv


def export_to_csv(tasks, filename="tasks_export.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "ID", "Title", "Description", "Status",
            "Priority", "Due Date", "Created At"
        ])

        for t in tasks:
            writer.writerow([
                t.id,
                t.title,
                t.description,
                t.status,
                t.priority,
                t.due_date,
                t.created_at
            ])