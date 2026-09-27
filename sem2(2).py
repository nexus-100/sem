import re

log_text = """
2026-09-26 08:00:12 INFO Connected to database at 10.0.0.5:5432
2026-09-26 08:01:33 WARN Connection pool usage at 85 percent
2026-09-26 08:02:47 INFO User 'admin' logged in from 192.168.1.10
2026-09-26 08:05:19 ERROR Failed to parse request body: invalid JSON
2026-09-26 08:05:20 INFO Retrying request id=4423 in 500ms
2026-09-26 08:07:55 DEBUG Cache hit ratio: 0.92
2026-09-26 08:10:00 INFO Scheduled job 'cleanup' started
2026-09-26 08:10:41 WARN Disk usage on /var/log reached 90 percent
2026-09-26 08:12:03 ERROR Timeout while calling payment-service after 5000ms
2026-09-26 08:12:04 INFO Fallback provider activated
2026-09-26 08:15:37 DEBUG GC pause: 42ms
2026-09-26 08:18:22 INFO User 'maria' uploaded file report.pdf
2026-09-26 08:20:11 WARN Deprecated API endpoint /v1/old called
2026-09-26 08:22:50 ERROR Unhandled exception in worker-3: NullPointerException
2026-09-26 08:22:51 INFO Worker-3 restarted by supervisor
2026-09-26 08:25:14 DEBUG Heartbeat sent to cluster node 10.0.0.7
2026-09-26 08:30:00 INFO Daily backup completed in 128 seconds
2026-09-26 08:31:45 ERROR Backup verification failed: checksum mismatch
"""

def get_errors_and_warnings(text: str) -> list[str]:
    """
    Выводит строки лога с уровнем ERROR или WARN.
    
    :param text: Текст лога.
    :return: Список строк с ошибками и предупреждениями.
    """
    if type(text) is not str:
        raise TypeError("Неверные входные данные! Ожидалась строка.")
    
    result = []
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (ERROR|WARN) (.+)"
    
    for line in text.splitlines():
        match = re.search(pattern, line)
        if match:
            result.append(f"{match.group(1)} {match.group(2)} {match.group(3)}")
    
    return result


def get_lines_with_ip(text: str) -> list[str]:
    """
    Выводит строки лога, в которых упоминаются IP-адреса.
    
    :param text: Текст лога.
    :return: Список строк с IP-адресами.
    """
    if type(text) is not str:
        raise TypeError("Неверные входные данные! Ожидалась строка.")
    
    result = []
    pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    
    for line in text.splitlines():
        match = re.search(pattern, line)
        if match:
            result.append(line)
    
    return result


print("ERROR и WARN:")
for line in get_errors_and_warnings(log_text):
    print(line)

print("Строки с IP-адресами:")
for line in get_lines_with_ip(log_text):
    print(line)
