# Ersilia Demo Repository
Demo repository for testing the Ersilia Model Hub incorporation pipeline, based on GitHub Actions

## Steps

### Create a model request at Ersilia

1. Go to the Ersilia main repository [issues page](https://github.com/ersilia-os/ersilia/issues).
2. Click on **New issue**. Then 🦠 **Model Request** (**Get started**)
3. For the purpose of this demo, you can use the following information:
   - 🦠 Model Request: Demo Malaria Model
   - **Model Name**: Demo Malaria Model
   - **Model Description**: Prediction of the antimalarial potential of small molecules. This model was originally trained on proprietary data from various sources, up to a total of >7M compounds. The training sets belong to Evotec, Johns Hopkins, MRCT, MMV - St. Jude, AZ, GSK, and St. Jude Vendor Library. In this implementation, we have used a teacher-student approach to train a surrogate model based on ChEMBL data (2M molecules) to provide a lite downloadable version of the original MAIP
   - **Slug**: demo-malaria-model
   - **Tag**: Malaria,P.falciparum
   - **Publication**: https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00487-2
   - **Code**: https://www.ebi.ac.uk/chembl/maip/
   - **License**: GPL-3.0

### Wait until model approval

1. The Ersilia team will revise your model requests and likely start a public discussion around it.
2. At some point, your model will be approved. You will see an `/approve` comment in the GitHub issues.
3. Approval will trigger some GitHub Actions. Eventually, the `ersilia-bot` will post an informative message in your issue. Importantly, this message will contain a link to a new model repository placeholder, named, for example, `ersilia-os/eosXabc`. This code is arbitrarily assigned by Ersilia and will change every time. You should not worry about creating one manually and you should never modify it.

### Fork the model repository

1. Go to the model repository page: https://github.com/ersilia-os/eosXabc, in this case.
2. Fork the repository to your username.
3. Clone the forked repository. This should create a `eosXabc` folder in your local filesystem.

### Use this demo model

1. For this demo, you have to clone the current repository (`ersilia-os/eos-demo`). This will create an `eos-demo` folder in your local filesystem.
2. Run the following script to populate your forked model with the demo data: `python /path/to/eos-demo/populate.py /path/to/eosXabc`.
3. Your `eosXabc` has been populated with model parameters, dependencies and extra metadata. It is now ready for commit.

### Make a pull request to Ersilia

1. Commit changes and push changes to `eosXabc`.
2. Open a PR to the `main` branch at `ersilia-os/eosXabc`. GitHub Actions workflows will be triggered to ensure that your code works as expected.

### Wait until model is merged

1. The Ersilia team will revise your PR and merge it eventually. More GitHub Actions workflows will be triggered at this point.
2. Once the model is merged, you should see it in [Ersilia's AirTable](https://airtable.com/shrNc3sTtTA3QeEZu).

### Assist with curation and publication

1. The `ersilia-bot` will open a new issue at `ersilia-os/eosXabc`. As you will see, someone from the Ersilia community will be assigned as a reviewer of the model.
2. If you are a member of the [Ersilia Slack workspace](https://ersilia-workspace.slack.com/), then you may also see activity triggered around your model.

## Test the model

You can test the model following these steps:

### Fetch the model

To run the model locally, you can fetch is with the `fetch` command.
```bash
ersilia fetch esoXabc
```
### Run predictions

You can create an example file and run predictions easily:

```bash
ersilia serve eosXabc
ersilia example -f my_input.csv
ersilia api -i my_input -o my_output.csv
ersilia close
```
