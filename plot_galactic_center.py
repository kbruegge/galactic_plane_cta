from astropy.table import Table
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import click


plt.rcParams['axes.facecolor'] = 'black'


@click.command()
@click.argument('input_file', type=click.Path(dir_okay=False, exists=True))
@click.argument('output_file', type=click.Path(dir_okay=False))
def main(input_file, output_file):
    t = Table.read(input_file)
    coords = SkyCoord(t['RA'], t['DEC'], ).transform_to('galactic')
    fig, ax = plt.subplots()
    a = ax.scatter(coords.l, coords.b, s=t['ENERGY'], c=t['ENERGY'], alpha=0.3, norm=LogNorm(), cmap='inferno')
    ax.set_ylim([-10, 10])
    # ax.set_ylim([-10, 10])
    plt.colorbar(a)
    plt.savefig(output_file)
    # import IPython; IPython.embed()



if __name__ == '__main__':
    main()
