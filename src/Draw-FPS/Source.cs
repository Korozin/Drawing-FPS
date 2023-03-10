using System.Windows.Forms;
using System.Diagnostics;
using System;

namespace Draw_FPS
{
    public partial class Source : Form
    {

        double prevTime = 0.0;
        int frameCount = 0;
        string fpstext;
        Stopwatch sw;

        public Source()
        {
            InitializeComponent();

            //Setting
            this.TopMost = true;
        }

        private void Source_Load(object sender, System.EventArgs e)
        {
            FPSLabel.Text = "FPS: 0.0";
            sw = Stopwatch.StartNew();

            //END
            Application.Idle += Application_Idle;
        }

        private void Application_Idle(object sender, EventArgs e)
        {
            double currTime = sw.Elapsed.TotalSeconds;
            double timeInterval = currTime - prevTime;

            if (timeInterval >= 0.1)
            {
                double fps = frameCount / timeInterval;
                fpstext = string.Format("FPS: {0:F2}", fps);
                FPSLabel.Text = fpstext;
                frameCount = 0;
                prevTime = currTime;
            }
            frameCount++;
        }
    }
}
