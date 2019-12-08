using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace GundamList
{
    /// <summary>
    /// MainWindow.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void OnChanged(object sender, SelectionChangedEventArgs e)
        {
            ListViewItem item = (ListViewItem)List.SelectedItem;
            TextBlock t = (TextBlock)((StackPanel)item.Content).Children[0];


           
            try
            {
                BitmapImage bitmapimage = new BitmapImage(new Uri($"pack://application:,,,/GundamList;component/images/{t.Text}.png"));
                image.Source = bitmapimage;

            }
            catch(IOException)
            {
                image.Source = null;
            }
            //MessageBox.Show(item.Content);  
            
        }
    }
}
