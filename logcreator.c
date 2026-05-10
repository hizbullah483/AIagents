#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define DEFAULT_LINES 200000

static const char *levels[] = {"INFO", "WARNING", "ERROR"};

static const char *messages[] = {
    "User login successful",
    "Request processed in 120ms",
    "Database query executed",
    "Cache miss — fetching from DB",
    "Connection timeout on socket 4521",
    "Failed to write to disk",
    "Retrying connection to server",
    "Authentication token expired",
    "Disk usage above 90 percent — critical",
    "Service refused connection on port 8080",
    "Backup completed successfully",
    "Memory usage normal",
    "Thread pool exhausted — queuing request",
    "Network latency spike detected",
    "Configuration file loaded",
    "Scheduled job started",
    "Scheduled job finished",
    "User session terminated",
    "API rate limit reached — request dropped",
    "File not found — returning 404"
};

int main(int argc, char *argv[]) {
    int total = DEFAULT_LINES;
    if (argc >= 2) total = atoi(argv[1]);
    if (total <= 0) total = DEFAULT_LINES;

    FILE *fp = fopen("test_logs.log", "w");
    if (!fp) { perror("fopen"); return 1; }

    srand((unsigned)time(NULL));

    int n_levels   = sizeof(levels)   / sizeof(levels[0]);
    int n_messages = sizeof(messages) / sizeof(messages[0]);

    printf("Generating %d log lines →totest_logs.log \n", total);

    for (int i = 0; i < total; i++) {
        int r = rand() % 100;
        const char *level = (r < 60) ? levels[0] : (r < 85) ? levels[1] : levels[2];
        const char *msg   = messages[rand() % n_messages];

        int hh = rand() % 24, mm = rand() % 60, ss = rand() % 60;

        fprintf(fp, "2026-04-16 %02d:%02d:%02d [%-7s] %s\n",
                hh, mm, ss, level, msg);
    }

    fclose(fp);
    printf("Done.\n");
    return 0;
}
