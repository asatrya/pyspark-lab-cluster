# Pyspak Lab Cluster Using Docker, To Experiment With PySpark on Yarn

### Project Folder Tree

```
├── docker-compose.yml
├── Dockerfile
├── confs
│   ├── config
│   ├── core-site.xml
│   ├── hdfs-site.xml
│   ├── mapred-site.xml
│   ├── requirements.req
│   ├── slaves
│   ├── spark-defaults.conf
│   └── yarn-site.xml
├── datasets
│   └── retail-data
├── pyspark
│   └── count_glass.py
└── script_files
    └── bootstrap.sh
```



### Build and Run the cluster

```bash
docker-compose up -d --build
```

### Yarn resource manager UI

Access the Yarn resource manager UI using the following link : http://<your-ip>:8088/cluster/nodes

![yarn ui](img/yarn_rm_ui.png)

### Stopping the cluster

```
docker-compose down
```

