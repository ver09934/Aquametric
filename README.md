# aquametric

Stream stage monitoring.

## Sensor Code

The code running on the sensor units can be found in `/embedded`. Everything else is for running the website.
<!--
## TODO

* [x] Get submission to separate unit files working
    * [x] Based off ID specified in post request
    * [ ] Don't break the server (write a separate submit function and swap once working)
* [x] Add unit configuration file for maps code to read
* [ ] Add URL args for sensor ID to sensor and plot pages
    * [ ] Graphs will also need an arg for metric to plot
    * [x] Add logfile conversion to CSV (on-the-fly)
        * [ ] Add data download links on unit pages
    * [ ] Plots will need to parse time strings into `datetime`s
* [ ] Improve log conversion and submit tests
    * [ ] Run the log conversion on the server
    * [ ] Pass file to convert as command line arg
    * [ ] Write to new file, `"{}-new.{}".format(basename, extension)`
* [ ] Add configuration based off environment variables
* [ ] Add "about" page (as linked-to on currently deployed sensor)
* [ ] Add cron job on server to back up data directory
    * Remove old test files once everything is migrated

* [ ] Sensor path pages and graph/log URLs will be based on sensor ID string
    * A json file will contain correlations between ID strings and prettyname/other metadata
* [ ] Graphs should show back to 24 or 48 hours before latest data point or earliest data, whichever is later
    * The URL args for these graphs are going to get epic
* Timezone parsing:
    * `datetime.datetime.strptime("2020-02-27T07:21:21.932Z", '%Y-%m-%dT%H:%M:%S.%f%z')`
    * `datetime.datetime.strptime("2020-02-27T07:21:21.932+05:30", '%Y-%m-%dT%H:%M:%S.%f%z')`
-->
## Setup

* Add config through environment variables (TODO)
* Add sensor list `JSON` file

    The following is an example `/sensors.json`:
    ```json
    {
        "001": {
            "lat": 42.784723,
            "lng": -73.842862,
            "prettyname": "Test Sensor 1",
            "img": "https://i.picsum.photos/id/724/500/300.jpg"
        },
        "002": {
            "lat": 43.100000,
            "lng": -74.10000,
            "prettyname": "Test Sensor 2",
            "img": "https://i.picsum.photos/id/323/500/300.jpg"
        }
    }
    ```
* Deploy a sensor unit (TODO: Get sensor code into version control)

## Running (Development)

```bash
$ chmod +x run.sh
$ ./run.sh
```

## Apache Adventures

I suspect that the problem was just the virtualhost configuration, but here are all the steps that were taken:

* `sudo apt install apache2-dev`
* install `mod_wsgi` in `venv`
* `sudo adduser $USER www-data`
* `sudo chown -R flask-project-dir www-data:www-data` and `sudo chmod -R g+rw flask-project-dir`
* Make dirs/files in code absolute using `os.path.join()` and `os.path.dirname(__file__)`
    * See <https://modwsgi.readthedocs.io/en/develop/user-guides/application-issues.html#application-working-directory>
    * See <https://modwsgi.readthedocs.io/en/develop/user-guides/application-issues.html#access-rights-of-apache-user>

## Python Notes

* `json.load` and `json.dump` use file objects
* `json.loads` and `json.dumps` take/return strings (that's what the "s" stands for)
* `readlines()` does not `rstrip()`, and `writelines()` does not add newlines

<!--
$("#info").fadeTo(300, 0.5);
$("#info").fadeTo(400, 1.0);
-->
