from astropy.table import Table, vstack
import click
from tqdm import tqdm
import os


@click.command()
@click.argument('files', nargs=-1)
@click.argument('output_file', type=click.Path(dir_okay=False, exists=False))
def main(files, output_file):

    if os.path.exists(output_file):
        click.confirm('Do you want overwrite existing file?', abort=True)
        os.remove(output_file)

    tables = []

    for f in tqdm(files):
        t = Table.read(f, hdu=1)
        t = t[t['MC_ID'] == 2]
        tables.append(t)
    gammas = vstack(tables, metadata_conflicts='silent')
    print('Writing {} events to file'.format(len(gammas)))
    gammas.write(output_file)


if __name__ == '__main__':
    main()
